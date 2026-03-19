

# toSet

Returns a Set of all elements.

```kotlin
fun <T> Array<out T>.toSet(): Set<T>(source)
```

```kotlin
fun main() {
    val array = arrayOf("apple", "banana", "apple")
    val set: Set<String> = array.toSet()
    println(set)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-set.html)

    