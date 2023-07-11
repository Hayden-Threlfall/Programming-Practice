use std::fs;
fn main() {
    let mut t: usize = 0;
    getline(&mut t);
    getline(&mut t);
    // skip first 2 lines
    let mut max = 0;
    rec(&mut max, &mut t);
    println!("Got line up to {}", t);
    println!("Max values added up {}", max);
}

fn rec(v: &mut i32, t: &mut usize) { //ignore all the ls's plus all the dir vars
                                     // Count the sizes ignore the x.txt

    //get new line // .contains(cd x) stop when find a cd ..

    // Find a cd x dive 1 more down if cd .. end
    // getnewline // skip $ ls line
    // while getnewline gives a number return += size of files
    // before you exit because cd.. check file dirrectory if less than or equal to 100,000 add to the end dirrectories size
}

const str: String = fs::read_to_string("src/input.txt").expect("Error in reading the file");

fn getline(t: &mut usize) -> &str {
    let lines = str.lines();
    let count: usize = 0;
    for line in lines {
        if count == t {
            t += 1;
            return line;
        }
        count += 1;
    }

    return "na";
}
