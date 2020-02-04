cppProgram = """#include<iostream>
using namespace std;
int main(){
    cout<<"Hello World";
    return 0;
}
"""

javaProgram = """class Main{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
"""

print(cppProgram)
print("~~~~~~~~~")
print(javaProgram)

file1 = open("/Users/ishantkumar/Downloads/MyApp.cpp", "w")
file1.write(cppProgram)
file1.close()

file2 = open("/Users/ishantkumar/Downloads/MyApp.java", "w")
file2.write(javaProgram)
file2.close()

print(">> PROGRAMS CREATED")


# Assignment
# Generate Hello World Program for these Languages:
# 1. Dart
# 2. Go     (https://tour.golang.org/welcome/1)
# 3. Kotlin
# 4. Scala
# 5. JavaScript and TypeScript

# PS: In all the languages above implement Insertion Sort and than generate programs

