# Class7-Python-Module-Week4

## 1. School

1. Create a `School` class with instance attribute `capacity`.
2. Add `students` as the class attribute. This will be a list and keep track of the students in the school.
3. Create a `Student` class with attributes: `name`, `age`, `gender`
4. Add `__str__` method to this class to print the objects.
6. Add `add_student` method to the class. If capacity is full print error message else add the student.
7. Add `print_students` method to print the all existing students. Loop through the students list and print each student object.
8. Create a `School` object and threee students, add first 2 students to school. Print students and afterwards try to add the third student.
9. Use `__dict__` method to see attributes

## 2. Rectangle

1. Write a `Rectangle` class, allowing you to build a rectangle with `length` and `width` attributes.
2. Create a `perimeter()` method to calculate the perimeter of the rectangle and an `area()` method to calculate the area of ​​the rectangle.
3. Create a method `display()` that displays the length, width, perimeter and area of an object created using an instantiation on `Rectangle` class.
4. Create a `Parallelepipede` child class inheriting from the `Rectangle` class and with a `height` attribute and another `volume()` method to calculate the volume of the `Parallelepiped`.

## 3. BankAccount

1. Create a Python class called  `BankAccount`  which represents a bank account, having as attributes:  `accountNumber`,  `name` , `balance`.
2.  Create a  **constructor**  with parameters:  `accountNumber`, `name`, `balance`.
3.  Create a  `deposit()`  method which manages the deposit actions. (deposit() method will take parameter d and you will increase the balance with the amount d)
4.  Create a  `withdrawal()` method which manages withdrawals actions. (withdrawal() method will take parameter w, you will reduce the amount of balance with w, if w is larger than the balance: then print `Impossible operation! Insufficient balance!"`)
5.  Create a `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account. (When this method is called, the balance amount should reduce 5%)
6.  Create a  `display()` method to display account details.


## HackerRank Questions

1. Inheritance: https://www.hackerrank.com/challenges/inheritance/problem
  
2. Classes: Dealing with Complex Numbers: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
