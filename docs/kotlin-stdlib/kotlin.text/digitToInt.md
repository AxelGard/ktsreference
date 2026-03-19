

# digitToInt

Returns the numeric value of the decimal digit that this Char represents. Throws an exception if this Char is not a valid decimal digit.

```kotlin
fun Char.digitToInt(): Int(source)
```

```kotlin
fun main() {
    val digit: Char = '9'
    val number = digit.digitToInt()
    println("The numeric value of '$digit' is $number")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/digit-to-int.html)

    