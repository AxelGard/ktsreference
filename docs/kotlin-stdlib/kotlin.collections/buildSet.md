

# buildSet

Builds a new read-only Set by populating a MutableSet using the given builderAction and returning a read-only set with the same elements.

```kotlin
inline fun <E> buildSet(builderAction: MutableSet<E>.() -> Unit): Set<E>(source)
```

```kotlin
fun main() {
    val fruits: Set<String> = buildSet {
        add("apple")
        add("banana")
        add("orange")
    }
    println(fruits) // [apple, banana, orange]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/build-set.html)

    