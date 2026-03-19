

# removeSurrounding

When this char sequence starts with the given prefix and ends with the given suffix, returns a new char sequence having both the given prefix and suffix removed. Otherwise, returns a new char sequence with the same characters.

```kotlin
fun CharSequence.removeSurrounding(prefix: CharSequence, suffix: CharSequence): CharSequence(source)
```

```kotlin
fun main() {
    val original = "\"Hello, world!\""
    val trimmed = original.removeSurrounding("\"", "\"")
    println(trimmed)            // Prints: Hello, world!

    val notTrimmed = "Hello, world!"
    println(notTrimmed.removeSurrounding("\"", "\""))  // Prints: Hello, world!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/remove-surrounding.html)

    