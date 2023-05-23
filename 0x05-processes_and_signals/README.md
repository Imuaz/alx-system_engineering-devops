# 0x05. Processes and signals:signal_strength:

**INRODUCTION**

The project covered several important aspects related to processes and signals. It started by explaining what a PID (Process ID) is and provided an understanding of processes in an operating system. Furthermore, it included information on how to find a process's PID and how to terminate or kill a process. The project also explored the concept of signals and their role in process communication. Specifically, it highlighted the significance of two signals that cannot be ignored. Overall, this project provided comprehensive insights into processes, PIDs, signals, and their practical implications in operating systems.

## Resources:books:
***Read or watch:***
- [Linux PID](http://www.linfo.org/pid.html)
- [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
- [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
- [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
***man or help:***
- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`

## More Info:information_source:
- If you want to know more and learn about all signals, check out [this article](https://www.computerhope.com/unix/signals.htm).

## Requirements:round_pushpin:

**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- Bash scripts must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of your Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:

**0. What is my PID**
- [0-what-is-my-pid](./0-what-is-my-pid): Bash script that displays its own PID.

**1. List your processes**
- [1-list_your_processes](./1-list_your_processes): Bash script that displays a list of currently running processes.
  - it shows all processes, for all users, including those which might not have a TTY
  - it display in a user-oriented format
  - shows process hierarchy

**2. Show your Bash PID**
- [2-show_your_bash_pid](./2-show_your_bash_pid): Bash script that displays lines containing the `bash` word using previous task command, thus, making it easily to get the PID of a Bash process.
  - it does not using `pgrep`
  - The third line of the script shows be `# shellcheck disable=SC2009` (for more info about ignoring shellcheck error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))

**3. Show your Bash PID made easy**
- [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy): Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
  - it is not Allowed to use `ps`

**4. To infinity and beyond**
- [4-to_infinity_and_beyond](./4-to_infinity_and_beyond): Bash script that displays `To infinity and beyond` indefinitely.
  - it adds a `sleep 2` in between each iteration of the loop.

**5. Don't stop me now!**
- [5-dont_stop_me_now](./5-dont_stop_me_now): Bash script that stops `4-to_infinity_and_beyond` process.
  - it uses `kill`

**6. Stop me if you can**
- [6-stop_me_if_you_can](./6-stop_me_if_you_can): Bash script that stops `4-to_infinity_and_beyond` process.
  - It is not allowed to use `kill` or `killall`

**7. Highlander**
- [7-highlander](./7-highlander): Bash script that displays:
  - `To infinity and beyond` indefinitely
  - With a `sleep 2` in between each iteration
  - `I am invincible!!!` when receiving a `SIGTERM` signal

**8. Beheaded process**
- [8-beheaded_process](./8-beheaded_process): Bash script that kills the process `7-highlander`.

**9. Process and PID file**
- [100-process_and_pid_file](./100-process_and_pid_file): Bash script that:
  - Creates the file `/var/run/myscript.pid` containing its PID
  - Displays `To infinity and beyond` indefinitely
  - Displays `I hate the kill command` when receiving a `SIGTERM` signal
  - Displays `Y U no love me?!` when receiving a `SIGINT` signal
  - Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

**10. Manage my process**
- read:
  - [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
  - [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
  - [Daemon](https://en.m.wikipedia.org/wiki/Daemon_(computing))
  - [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)
  - man:`sudo`
- Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.
- [manage_my_process](./manage_my_process): Bash script that:
  - Indefinitely writes `I am alive!` to the file `/tmp/my_process`
  - In between every `I am alive!` message, the program pauses for 2 seconds
- [101-manage_my_process](./101-manage_my_process): Bash (init) script that manages `manage_my_process`.
  - When passing the argument `start`:
    - it starts `manage_my_process`
    - it creates a file containing its PID in `/var/run/my_process.pid`
    - it displays `manage_my_process started`
  - When passing the argument `stop`:
    - it stops `manage_my_process`,
    - deletes the file `/var/run/my_process.pid`,
    - displays `manage_my_process stopped`
  - When passing the argument `restart`:
    - it stops `manage_my_process`,
    - deletes the file `/var/run/my_process.pid`,
    - starts `manage_my_process`,
    - creates a file containing its PID in `/var/run/my_process.pid`, and
    - displays `manage_my_process restarted`
  - It displays Usage: `manage_my_process {start|stop|restart}` if any other argument or no argument is passed
- Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

**11. Zombie**
- Read [what a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).
- [102-zombie.c](./102-zombie.c): C program that creates 5 zombie processes.
  - For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
  - the code uses the Betty style. It may be checked using `betty-style.pl` and `betty-doc.pl`
  - When the code is done creating the parent process and the zombies,it uses the function bellow
  ```
  int infinite_while(void)
  {
      while (1)
      {
          sleep(1);
      }
      return (0);
  }
  ```

  :+1:
