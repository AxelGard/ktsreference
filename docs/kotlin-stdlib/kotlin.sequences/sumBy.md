

# sumBy

Warning since 1.5

```kotlin
inline fun <T> Sequence<T>.sumBy(selector: (T) -> Int): Int(source)
```

```kotlin
fun main() {
    val words = listOf("apple", "banana", "cherry")
    val totalLength = words.asSequence().sumBy { it.length }
    println(totalLength)  // prints 16
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sum-by.html)

    