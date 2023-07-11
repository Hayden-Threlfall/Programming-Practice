use core::ptr::copy;
fn main() {
    // How I would do this.
    // What needs to happen is you need 3 arrays
    // 1 is the input of the string to keep the order // unmutable
    // The second is the postion in the order of the first values in the 3rd array
    // The thid is how the final array will look with the all the values circualary rotated

    let initial: Vec<i32> = vec![1, 2, -3, 3, -2, 0, 4];
    let mut pos: Vec<usize> = vec![0, 1, 2, 3, 4, 5, 6];
    let mut out: Vec<i32> = vec![1, 2, -3, 3, -2, 0, 4];
    rot(&mut out, &mut pos, 0);
    print!("[");
    for l in out {
        print!("{}, ", l);
    }
    print!("]");
    println!();
}

fn rot(arr: &mut Vec<i32>, pos: &mut Vec<usize>, p: usize) {
    let t: i32 = arr[p];
    if t > 0 {
        //
        shift(arr, t, p);
        shift(pos, t, p);
    } else if t < 0 {
        //
        antishift(arr, t, p);
        antishift(pos, pos[p], p);
    } else {
        // Do noting
    }
}

fn shift(arr: &mut Vec<i32>, val: i32, p: usize) {
    arr[p];
}

fn antishift(arr: &mut Vec<i32>, val: i32, p: usize) {
    //
}
