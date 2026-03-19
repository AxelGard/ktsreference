

# toBooleanStrict

Returns true if the content of this string is equal to the word "true", false if it is equal to "false", and throws an exception otherwise.

```kotlin
fun String.toBooleanStrict(): Boolean(source)
```

```kotlin
fun main() {
    val trueStr   = "true"
    val falseStr  = "false"
    val invalidStr = "yes"

    println(trueStr.toBooleanStrict())    // prints: true
    println(falseStr.toBooleanStrict())   // prints: false

    try {
        println(invalidStr.toBooleanStrict())
    } catch (e: IllegalArgumentException) {
        println("Invalid boolean string: ${e.message}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-boolean-strict.html)

    