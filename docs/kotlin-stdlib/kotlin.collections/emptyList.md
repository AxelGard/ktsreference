

# emptyList

Returns an empty read-only list.  The returned list is serializable (JVM).

```kotlin
fun <T> emptyList(): List<T>(source)
```

```kotlin
fun main() {
    // Create an empty list of strings
    val emptyStrings: List<String> = emptyList()

    // Verify that the list is indeed empty
    println("Size: ${emptyStrings.size}")  // Output: Size: 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/empty-list.html)

    