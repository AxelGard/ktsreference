

# Iterable

Given an iterator function constructs an Iterable instance that returns values through the Iterator provided by that function.

```kotlin
inline fun <T> Iterable(crossinline iterator: () -> Iterator<T>): Iterable<T>(source)
```

```kotlin
fun main() {
    // Create an Iterable by supplying a lambda that returns an Iterator
    val numbers = Iterable<Int> { listOf(1, 2, 3, 4, 5).iterator() }

    // Iterate over the Iterable just like a regular collection
    for (n in numbers) {
        println(n)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable.html)

    