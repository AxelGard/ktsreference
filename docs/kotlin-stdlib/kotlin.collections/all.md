

# all

Returns true if all elements match the given predicate.

```kotlin
inline fun <T> Array<out T>.all(predicate: (T) -> Boolean): Boolean(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "banana", "cherry")
    val allContainLetterA = words.all { it.contains('a') }
    println(allContainLetterA) // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/all.html)

    