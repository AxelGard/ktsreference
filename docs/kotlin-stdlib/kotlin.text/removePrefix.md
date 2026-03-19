

# removePrefix

If this char sequence starts with the given prefix, returns a new char sequence with the prefix removed. Otherwise, returns a new char sequence with the same characters.

```kotlin
fun CharSequence.removePrefix(prefix: CharSequence): CharSequence(source)
```

fun main() {
    val original = "Hello, Kotlin!"
    val withoutHello = original.removePrefix("Hello, ")
    println(withoutHello) // Kotlin!
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/remove-prefix.html)

    