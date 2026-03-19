

# splitToSequence

Splits this char sequence to a sequence of strings around occurrences of the specified delimiters.

```kotlin
fun CharSequence.splitToSequence(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): Sequence<String>(source)
```

```kotlin
val sentence = "Kotlin,Java;Python,Rust"
val words = sentence.splitToSequence(",", ";")

words.forEach { println(it) }   // prints each word separately
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/split-to-sequence.html)

    