

# buildList

Builds a new read-only List by populating a MutableList using the given builderAction and returning a read-only list with the same elements.

```kotlin
inline fun <E> buildList(builderAction: MutableList<E>.() -> Unit): List<E>(source)
```

```kotlin
fun main() {
    val fruits = buildList {
        add("Apple")
        add("Banana")
        add("Cherry")
    }
    println(fruits)   // Output: [Apple, Banana, Cherry]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/build-list.html)

    