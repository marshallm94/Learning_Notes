# How do I permanently add external storage to a Linux machine?

* [Very helpful video](https://www.youtube.com/watch?v=eQZdPlMH-X8)
* [How to use `parted`](https://www.tecmint.com/add-disk-larger-than-2tb-to-an-existing-linux/)

0. Delete old partitions (if they exist).
    * run `$ sudo fdisk -l` and find the location of the drive you have attached. Look for the `Disk` with the expected
      number of bytes available:
        * For, example, the 5 TB (`5000981077504 bytes`) HD I attached is showing up as `/dev/sda` and it has 1
          partition at `/dev/sda1`. 
        ```bash
        $ sudo fdisk -l
        Disk /dev/sda: 4.6 TiB, 5000981077504 bytes, 9767541167 sectors
        Disk model: Portable        
        Units: sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 4096 bytes
        I/O size (minimum/optimal): 4096 bytes / 4096 bytes
        Disklabel type: gpt
        Disk identifier: 285B58D2-268E-499A-BFD2-201B5F9B181E

        Device     Start        End    Sectors  Size Type
        /dev/sda1   2048 9767540735 9767538688  4.6T Linux filesystem
        ```
        * run `$ sudo fdisk <path_to_external_disk>` (`$ sudo fdisk /dev/sda` in example), and continuously
          press `d` until all partitions are deleted. Type `w` to write the changes.
        * Once complete, run `$ sudo fdisk -l` again to confirm your changes worked. You should see the same output as
          above, **except there shouldn't be any "Device"s listed**:
          ```bash
          $ sudo fdisk -l
          Disk /dev/sda: 4.6 TiB, 5000981077504 bytes, 9767541167 sectors
          Disk model: Portable        
          Units: sectors of 1 * 512 = 512 bytes
          Sector size (logical/physical): 512 bytes / 4096 bytes
          I/O size (minimum/optimal): 4096 bytes / 4096 bytes
          Disklabel type: gpt
          Disk identifier: 285B58D2-268E-499A-BFD2-201B5F9B181E
          ```
1. Create a new partition.
    * run `$ sudo parted <path_to_external_disk>` (`$ sudo parted /dev/sda` in example) to start the GNU `parted`
      program:
        * run `(parted) mklabel gpt`
        * run `(parted) mkpart primary 0GB <desired_amount_of_space>`
            * E.g. `(parted) mkpart primary 0GB 5TB`
        * run `(parted) quit` to persist your changes.
2. Create new filesystem.
    * run `$ sudo mkfs.ext4 /dev/sda1`
        * **Make sure you specifiy the path to the partition (`/dev/sda1`) and not the drive (`/dev/sda`) itself.** 
3. Create a directory to to which the drive should be mounted.
    * Drives that are going to be considered permanent should be mounted to a subdirectory of `/mnt/`.
        * run `$ sudo mkdir /mnt/<dir_name_you_want>`
4. Add the external drive to the `/etc/fstab` file (`fstab` = file system table) so it is mounted at boot.
    * run `$ sudo blkid` and copy the `UUID` (**without the parentheses**) that corresponds to the partition you
      created.
    * edit the `/etc/fstab` file.
        * run `$ sudo vi /etc/fstab`
        * Add the following line:
        ```bash
        # ...other PARTUUID lines...
        UUID=<random_UUD_copied_from_above> <path_to_mount_directory> <filesystem_type> defaults 0 1
        # for example
        UUID=fe6b201c-bd1a-4843-a88a-167db8746d89 /mnt/seagate_5tb_extdrive ext4 defaults 0 1
        ```
5. Run `$ sudo mount -a` to mount the drive
    * After you have run the above, run `$ df -H` and you should see the new filesystem pop up:
        * For example (second line from bottom):
        ```bash
        $ df -H
        Filesystem      Size  Used Avail Use% Mounted on
        /dev/root        32G   22G  8.9G  71% /
        devtmpfs        1.9G     0  1.9G   0% /dev
        tmpfs           2.1G     0  2.1G   0% /dev/shm
        tmpfs           2.1G   51M  2.0G   3% /run
        tmpfs           5.3M  4.1k  5.3M   1% /run/lock
        tmpfs           2.1G     0  2.1G   0% /sys/fs/cgroup
        /dev/mmcblk0p1  265M   53M  213M  20% /boot
        /dev/sda1       5.0T  1.4G  4.8T   1% /mnt/seagate_5tb_extdrive
        tmpfs           403M     0  403M   0% /run/user/1000
        ```
6. Set the permissions appropriately on `/mnt/<path_to_mount_directory>/` (e.g. `/mnt/seagate_5tb_extdrive/`) so users
   can read/write/execute what they need to.
7. Test that you're setup persists after a reboot.
    * run `$ sudo reboot` to restart the machine. Once it is backup, run `$ df -H` again and you should see the same
      output as that in step 6.
