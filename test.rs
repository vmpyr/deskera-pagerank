use std::io::{self, Write};
use std::process::Command;

fn main() {
    print!("Enter a command: ");
    io::stdout().flush().unwrap();

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let input = input.trim();

    let output = match Command::new("sh").arg("-c").arg(input).output() {
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
