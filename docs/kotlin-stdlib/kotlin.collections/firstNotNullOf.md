

# firstNotNullOf

Returns the first non-null value produced by transform function being applied to elements of this array in iteration order, or throws NoSuchElementException if no non-null value was produced.

```kotlin
inline fun <T, R : Any> Array<out T>.firstNotNullOf(transform: (T) -> R?): R(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 3, 4, 5)
    val firstEven = numbers.firstNotNullOf { if (it % 2 == 0) it else null }
    println(firstEven) // 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first-not-null-of.html)

    