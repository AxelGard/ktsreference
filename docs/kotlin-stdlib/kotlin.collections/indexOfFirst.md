

# indexOfFirst

Returns index of the first element matching the given predicate, or -1 if the array does not contain such element.

```kotlin
inline fun <T> Array<out T>.indexOfFirst(predicate: (T) -> Boolean): Int(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("apple", "banana", "cherry", "date")
    val index = fruits.indexOfFirst { it.startsWith("c") }  // returns 2
    println("First fruit starting with 'c' is at index: $index")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index-of-first.html)

    