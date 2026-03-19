

# toBooleanStrictOrNull

Returns true if the content of this string is equal to the word "true", false if it is equal to "false", and null otherwise.

```kotlin
fun String.toBooleanStrictOrNull(): Boolean?(source)
```

```kotlin
fun main() {
    val testStrings = listOf("true", "false", "True", "yes", "")
    for (s in testStrings) {
        val result = s.toBooleanStrictOrNull()
        println("Input: \"$s\" → $result")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-boolean-strict-or-null.html)

    