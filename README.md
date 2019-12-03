# wrap
Pipe long terminal lines to Wrap and it will line wrap them at a column you specify.

## Performance

In general, the Rust version performed 2x as fast as the Python version.

```bash
$ measure-command { ls -lah ~ | rust 40 }
$ measure-command { ls -lah ~ | wrap 40 }
$ measure-command { ls -lah ~ | ./wrap 40 }
```

Over 100 runs, here are the metrics on my machine (Mac Pro v10.14.6, 2.3 GHz i5,
 8GB 2133 MHz LPDDR3).

| Language | Average Ms | Max Ms | Min Ms |
| -------- | ---------- | ------ | ------ |
| Rust     | 28.82      | 39     | 25     |
| Nim      | 29.43      | 39     | 25     |
| Python   | 57.89      | 64     | 55     |

To summarize, the Rust version is 2x faster than Python, and only 0.02x faster
than Nim.
