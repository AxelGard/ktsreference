

# toULong

Parses the string as a ULong number and returns the result.

```kotlin
fun String.toULong(): ULong(source)
```

```kotlin
fun main() {
    val stringNumber = "12345678901234567890"
    val uLongValue: ULong = stringNumber.toULong()
    println("ULong value: $uLongValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-long.html)

    