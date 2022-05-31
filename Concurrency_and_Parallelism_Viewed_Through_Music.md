# Concurrency & Parallelism Through the Lens of Music

Music domain (piano being the instrument of choice):
* notes
* chords
* piece(song)
* hand (singular)
* hands (both)
* fingers (hardware?)
* fingering

Computer Science domain:
* concurrency
* parallelism
* threading
* multiprocessing
* asyncronous I/O
* process/task/threads
* processor
* core
* hyperthreading

# Initial Guesses

* `Music Domain <--> Computer Science Domain`
* `fingers <--> cores`
* `hands <--> processor`

**<u>How to read the below table:</u>**

"`X` *is/are to the* **Music Domain** in the same way the `Y` *is/are to the* **Computer Science Domain**"

Further definitions:

* "People create programs to direct processes." - SICP
  * Addition: "People create programs *which resemble solutions to problems* to direct *computational* process"
  * Addition: "People create programs to direct *computational* process *whose outcome solves a problem*."

`Problem <--> Programs <--> Process`

`Real World <--> Programs <--> Computational World`



| `X`            | `Y`                  |
| -------------- | -------------------- |
| Pieces (songs) | Application Programs |
| Chords         | Parallelism          |
| Notes          | Concurrency          |
|                | Synchronous          |
|                | Asynchronous         |
| Fingers        | Cores                |
| Hands          | Processors           |
