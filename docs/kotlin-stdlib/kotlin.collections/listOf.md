

# listOf

Returns a new read-only list of given elements.  The returned list is serializable (JVM).

```kotlin
fun <T> listOf(vararg elements: T): List<T>(source)(source)
```

```kotlin
fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")
    println(fruits)          // Output: [Apple, Banana, Cherry]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/list-of.html)

    