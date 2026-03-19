

# asIterable

Creates an Iterable instance that wraps the original array returning its elements when being iterated.

```kotlin
fun <T> Array<out T>.asIterable(): Iterable<T>(source)
```

```kotlin
val words = arrayOf("kotlin", "java", "swift", "python")
for (word in words.asIterable()) {
    println(word)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-iterable.html)

    