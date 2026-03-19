

# toDouble

Parses the string as a Double number and returns the result.

```kotlin
expect fun String.toDouble(): Double(source)
```

```kotlin
fun main() {
    val numberString = "123.456"
    val number: Double = numberString.toDouble()
    println("The parsed double is: $number")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-double.html)

    