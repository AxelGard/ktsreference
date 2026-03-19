

# mapIndexedTo

Applies the given transform function to each element and its index in the original array and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Array<out T>.mapIndexedTo(destination: C, transform: (index: Int, T) -> R): C(source)
```

```kotlin
val words = arrayOf("apple", "banana", "cherry")

val result = mutableListOf<String>().apply {
    words.mapIndexedTo(this) { index, word ->
        "$index: $word"
    }
}

println(result) // Output: [0: apple, 1: banana, 2: cherry]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-indexed-to.html)

    