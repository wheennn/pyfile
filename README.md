# pyfile

## About the project

**pyfile** is a minimalistic TUI file explorer with cross-platform support. Can be used as a small dev utility for fast file opening with just a few keys. Written in **Python** using **keyboard** library and few other modules.

## Controls

### Terminal commands

| Command              | Action                       |
|----------------------|------------------------------|
| pyfile \<dir\>       | Open the specified directory |
| pyfile -current (-c) | Open current directory       |

### Inline control buttons

| Button | Action                        |
|--------|-------------------------------|
| Enter  | Enter a folder or open a file |
| Q      | Go to parent directory        |
| ↑      | Move selection up             |
| ↓      | Move selection down           |

## Architecture

```
pyfile/
├── pyproject.toml  
├── pyfile_package/  
│   ├── __init__.py  
│   └── main.py
...
```

## How to run

### Requirements

> Python  3.14+  
> keyboard 0.13.5+  

### Instruction

1. Clone the repository

```bash
git clone 'https://github.com/wheennn/pyfile.git'
```

2. Open the directory & install package

```cmd
cd pyfile
pip install .
```

3. Open console & enter `pyfile <dir>` or `pyfile -c` to get started and browse your files!

## Tech Stack

**Language**: Python  
**Library**: keyboard  
**Modules**: os, time, platform, sys

## Contributing

 Feedback & support are appreciated — any review, fork, issue opening or pull request would incredibly help in development of project!

## License

[MIT License](https://github.com/wheennn/pyfile/blob/main/LICENSE)
