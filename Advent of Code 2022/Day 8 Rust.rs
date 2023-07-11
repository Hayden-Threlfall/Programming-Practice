use std::fs;

fn main() {
    let str: String = fs::read_to_string("src/input.txt").expect("Error in reading the file");
    //const size: usize = ((str.len() as f32).sqrt()) as usize;
    const SIZE: usize = 99; // 5; // I have to set the size manualy because I have yet to find a way around the array size reqiring a constant, could be fixed with a vector
    let mut arr = [[0; SIZE]; SIZE];
    let mut seen = [[false; SIZE]; SIZE];
    let lines = str.lines();
    let mut i = 0;
    let mut j = 0;
    for line in lines {
        for char in line.chars() {
            arr[i][j] = char as i32 - 0x30;
            j += 1;
        }
        j = 0;
        i += 1;
    }
    // Old code to make the outside edges all true
    for i in 0..SIZE {
        seen[0][i] = true;
        seen[SIZE - 1][i] = true;
        seen[i][0] = true;
        seen[i][SIZE - 1] = true;
    }

    // Better Implementation looking at each object until i = -1; Optimization will be low, but later problem
    let mut i2;
    let mut j2;
    let mut bool: bool = true;
    let mut con;
    let mut counter = [0; 4];
    let mut max = 0;

    for i in 1..SIZE - 1 {
        for j in 1..SIZE - 1 {
            counter = [0, 0, 0, 0];
            i2 = i;
            j2 = j;

            bool = true;
            while i2 > 0 {
                counter[0] += 1;
                if arr[i][j] <= arr[i2 - 1][j]
                /* && !seen[i][j] */
                {
                    bool = false;
                    break;
                }
                i2 -= 1;
            }
            if seen[i][j] != true {
                seen[i][j] = bool;
            }

            bool = true;
            while j2 > 0 {
                counter[1] += 1;
                if arr[i][j] <= arr[i][j2 - 1]
                /* && !seen[i][j] */
                {
                    bool = false;
                    break;
                }
                j2 -= 1;
            }
            if seen[i][j] != true {
                seen[i][j] = bool;
            }

            i2 = i;
            j2 = j;
            bool = true;
            while i2 < SIZE - 1 {
                counter[2] += 1;
                if arr[i][j] <= arr[i2 + 1][j]
                /* && !seen[i][j] */
                {
                    bool = false;
                    break;
                }
                i2 += 1;
            }
            if seen[i][j] != true {
                seen[i][j] = bool;
            }

            bool = true;
            while j2 < SIZE - 1 {
                counter[3] += 1;
                if arr[i][j] <= arr[i][j2 + 1]
                /*/* && !seen[i][j] */ */
                {
                    bool = false;
                    break;
                }
                j2 += 1;
            }
            if seen[i][j] != true {
                seen[i][j] = bool;
            }

            con = 1;
            println!("The location: {}, {}: {}", i, j, arr[i][j]);
            println!("The vaues: ");
            for i in counter {
                con *= i;

                print!("{} ", i);
            }
            if con > max {
                max = con;
            }
            println!("The end result: {}\n, ", con);
        }
    }

    // // Printing the array
    // for i in arr {
    //     for j in i {
    //         print!("{}", j);
    //     }
    //     println!();
    // }

    //println!("\n\n");
    // End of code counter
    let mut count = 0;
    for i in seen {
        for j in i {
            if j == true {
                count += 1;
            }
            //print!("{} ", j);
        }
        //println!();
    }
    println!("Number of seen trees: {}", count);
    println!("Best location score: {}", max);
}
