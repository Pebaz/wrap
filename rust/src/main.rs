use std::env::args;
use std::process;
use std::io::{self, BufRead};

fn main() {
    let col = if let Some(col) = args().skip(1).next() {
        col.parse::<usize>().unwrap()
    } else {
        println!("Wrap long columns in a wide terminal.");
        println!("Usage: wrap <column>\nExample: ls -lah | wrap 60");
        process::exit(0);
    };

    let stdin = io::stdin();
    for each_line in stdin.lock().lines() {
        let mut line = each_line.unwrap();

        loop {
            if col >= line.len() {
                println!("{}", line);
                break;
            } else {
                let rest = line.split_off(col);
                println!("{}", line);
                line = rest;
            }
        }
    }
}
