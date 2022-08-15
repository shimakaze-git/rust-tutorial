// stdと呼ばれる標準ライブラリ
// io（入出力）ライブラリ
use std::cmp::Ordering;
use std::io;

use rand::Rng;
// use ferris_says::say;
// use std::io::{stdout, BufWriter};

fn main() {
    let x = 5;
    let y = 10;

    println!("x = {} and y = {}", x, y);

    println!("Guess the number!");

    // 乱数を生成
    let secret_number = rand::thread_rng().gen_range(1..101);
    // println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();
        // mut : mutable
        // Stringは標準ライブラリによって提供される文字列型で、
        // サイズが拡張可能な、UTF-8でエンコードされたテキスト片になる

        // ユーザの入力を受け取る
        // 標準入力ハンドルのread_lineメソッド
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        // プログラムが入力として読み込んだStringを実数型に変換
        // Stringインスタンスのtrimメソッドは文字列の先頭と末尾の空白をすべて削除
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        // .expect("Please type a number!");

        println!("You guessed: {}", guess);

        // 条件分岐式
        match guess.cmp(&secret_number) {
            // Less、Greater、Equalという列挙子
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
