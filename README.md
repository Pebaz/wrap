# wrap
Pipe long terminal lines to Wrap and it will line wrap them at a column you specify.

## Performance

In general, the Rust version performed 2x as fast as the Python version.

```bash
$ measure-command { ls -lah ~ | rust 40 }
$ measure-command { ls -lah ~ | wrap 40 }
```
