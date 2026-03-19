

# count

Returns the number of elements in this sequence.

```kotlin
fun <T> Sequence<T>.count(): Int(source)
```

```kotlin
fun main() {
    val words = listOf("kotlin", "java", "swift", "kotlin")
        .asSequence()          // Create a Sequence from a List
    val count = words.count() // Count all elements in the sequence
    println("Number of words: $count") // Prints: Number of words: 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/count.html)

    