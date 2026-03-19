

# toShortOrNull

Parses the string to a Short number or returns null if the string is not a valid representation of a Short.

```kotlin
fun String.toShortOrNull(): Short?(source)
```

```kotlin
fun main() {
    val input1 = "200"
    val input2 = "not a number"

    val short1: Short? = input1.toShortOrNull()
    val short2: Short? = input2.toShortOrNull()

    println(short1) // 200
    println(short2) // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-short-or-null.html)

    