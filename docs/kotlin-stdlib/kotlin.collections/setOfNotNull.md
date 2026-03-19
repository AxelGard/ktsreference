

# setOfNotNull

Returns a new read-only set either with single given element, if it is not null, or empty set if the element is null. The returned set is serializable (JVM).

```kotlin
fun <T : Any> setOfNotNull(element: T?): Set<T>(source)(source)
```

```kotlin
fun main() {
    val nonEmptySet = setOfNotNull("Kotlin")
    val emptySet = setOfNotNull<String>(null)

    println(nonEmptySet) // [Kotlin]
    println(emptySet)    // []
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/set-of-not-null.html)

    