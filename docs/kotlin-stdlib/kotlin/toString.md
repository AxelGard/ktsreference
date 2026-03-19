

# toString

Returns a string representation of the object. Can be called with a null receiver, in which case it returns the string "null".

```kotlin
expect fun Any?.toString(): String(source)
```

```kotlin
fun main() {
    val nullableValue: Any? = null
    println(nullableValue.toString()) // Prints: null

    val nonNullValue: Any? = "Kotlin"
    println(nonNullValue.toString()) // Prints: Kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/to-string.html)

    