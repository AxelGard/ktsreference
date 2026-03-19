

# takeWhile

Returns a list containing first elements satisfying the given predicate.

```kotlin
inline fun <T> Array<out T>.takeWhile(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)
    val result = numbers.takeWhile { it <= 3 }
    println(result) // [1, 2, 3]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/take-while.html)

    