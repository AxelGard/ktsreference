

# lastOrNull

Returns the last element, or null if the array is empty.

```kotlin
fun <T> Array<out T>.lastOrNull(): T?(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "banana", "cherry")
    println(words.lastOrNull())   // Output: cherry

    val empty = arrayOf<String>()
    println(empty.lastOrNull())   // Output: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/last-or-null.html)

    