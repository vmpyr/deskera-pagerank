use std::io::{self, Write};
use std::process::Command;

fn main() {
    print!("Enter path to script: ");
    io::stdout().flush().unwrap();

    let mut scr = String::new();
    io::stdin().read_line(&mut scr).unwrap();
    let scr = scr.trim();

    print!("Enter path to .graphml file: ");
    io::stdout().flush().unwrap();

    let mut path = String::new();
    io::stdin().read_line(&mut path).unwrap();
    let path = path.trim();

    let output = match Command::new(scr).arg(path).output() {
        Ok(output) => output,
        Err(_) => todo!()
    };

    let stdout = String::from_utf8_lossy(&output.stdout);
    let stderr = String::from_utf8_lossy(&output.stderr);

    if !stdout.is_empty() {
        println!("Standard Output:\n{}", stdout);
    }

    if !stderr.is_empty() {
        println!("Standard Error:\n{}", stderr);
    }
}
