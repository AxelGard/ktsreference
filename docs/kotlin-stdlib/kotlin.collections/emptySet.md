

# emptySet

Returns an empty read-only set.  The returned set is serializable (JVM).

```kotlin
fun <T> emptySet(): Set<T>(source)
```

```kotlin
val emptySet: Set<String> = emptySet()
println(emptySet.isEmpty()) // true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/empty-set.html)

    