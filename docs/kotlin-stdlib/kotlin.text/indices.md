

# indices

Returns the range of valid character indices for this char sequence.

```kotlin
val CharSequence.indices: IntRange(source)
```

```kotlin
fun main() {
    val word = "Kotlin"
    for (index in word.indices) {
        println("Character at index $index: ${word[index]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/indices.html)

    