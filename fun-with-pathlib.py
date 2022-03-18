#!/usr/bin/env python3
from pathlib import Path
import pathlib
import os
import shutil

# https://docs.python.org/3/library/pathlib.html

p = Path()
for x in p.iterdir():
    print(x.resolve(), type(x), x.is_dir(), x.owner, x.group(), x.exists())
    x.chmod(0o0644)
    # stat = x.stat()
    # x.rename("name.txt")
    # text = x.read_text()
    # bytes = x.write_text(text)
    # dirname = p.parent
    # basename = p.name
    # cwd = Path.cwd()
    
    # breakpoint()


ssh = Path("~") / ".ssh"
print(ssh)
print(ssh.resolve())

init = next(Path("/boot").glob("initramfs-linux*"))
print(init.suffix)

# ** means this directory and all subdirectories
#print(list(p.glob("**/*.py")))


script_dir = Path(__file__).parent.resolve()
print(script_dir)


p = Path("/opt")
assert type(p) == pathlib.PosixPath
p_str = os.fspath(p)
assert str(p.resolve()) == p_str
assert type(p_str) == str
assert p_str == p.as_posix()


test = Path("test")
if not test.exists():
    print(f"Creating {test}")
    test.mkdir(mode=0o0700, exist_ok=True)
    out = test / Path("file.txt")
    out.touch(mode=0o0700)
    out.write_text("heyho")
    out.unlink()
Path("test").rmdir()

# TODO: https://docs.python.org/3/library/shutil.html#shutil.rmtree
