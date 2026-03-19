

# toUInt

Parses the string as an UInt number and returns the result.

```kotlin
fun String.toUInt(): UInt(source)
```

```kotlin
fun main() {
    val decimalString = "123"
    val number: UInt = decimalString.toUInt()

    println("The UInt value is $number")  // Output: The UInt value is 123
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-int.html)

    