import string
import random
def id_generator():
    chars = string.ascii_lowercase + '_'
    return ''.join(random.choice(chars) for _ in range(16))

NUM_FUNCS = 1250000

ids = [id_generator() for _ in range(NUM_FUNCS)]

with open('dumbbench.c', 'w', newline='\n') as f:
    for name in ids:
        f.write(f'''\
// This is the {name} function!
int {name}(void) {{
    int x = 0;
    const char* z = "this is a string";
    for (int i = 0; i < 5; ++i)
        x += i;
    return x;
}}
''')

    f.write('''\
int main() {
    return 0;
}
''')


# Lua can only have 128k funcs per file (and luajit only 64k constants), so
# split up into many chunks. Maybe not quite fair? I dunno.
STEP = 31250
with open('dumbbench.lua', 'w', newline='\n') as f2:
    for i in range(0, NUM_FUNCS, STEP):
        f2.write(f"dofile 'dumbbench{i//STEP}.lua'\n")
        with open(f'dumbbench{i//STEP}.lua', 'w', newline='\n') as f:
            for name in ids[i:i+STEP]:
                f.write(f'''\
-- This is the {name} function!
function {name}()
    local x = 0
    local z = "this is a string";
    for i=0,4 do x=x+i
    end
    return x
end
''')



with open('dumbbench.luv', 'w', newline='\n') as f:
    for name in ids:
        f.write(f'''\
# This is the {name} function!
def int {name}():
    int x = 0
    str z = "this is a string"
    for i in range(5):
        x += i
    return x

''')

    f.write('''\
def int main():
    return 0
''')


with open('dumbbench.py', 'w', newline='\n') as f:
    for name in ids:
        f.write(f'''\
# This is the {name} function!
def {name}():
    x = 0
    z = "this is a string";
    for i in range(5):
        x += i
    return x

''')

with open('dumbbench.js', 'w', newline='\n') as f:
    for name in ids:
        f.write(f'''\
// This is the {name} function!
function {name}() {{
    var x = 0;
    var z = "this is a string";
    for (let i = 0; i < 5; step++)
        x += i;
    return x;
}}
''')

with open('dumbbench.rs', 'w', newline='\n') as f:
    f.write('#![allow(unused)]\n')
    f.write('#![allow(non_snake_case)]\n\n')
    for name in ids:
        f.write(f'''\
// This is the {name} function!
fn {name}() -> i32 {{
    let mut x = 0;
    let _z = "this is a string";
    for i in 0..5 {{
        x += i; }}
    return x;
}}
''')

    f.write('fn main() {}\n')
