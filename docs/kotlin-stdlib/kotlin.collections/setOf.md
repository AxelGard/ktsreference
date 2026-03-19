

# setOf

Returns a new read-only set with the given elements. Elements of the set are iterated in the order they were specified. The returned set is serializable (JVM).

```kotlin
fun <T> setOf(vararg elements: T): Set<T>(source)(source)
```

```kotlin
fun main() {
    val colors = setOf("red", "green", "blue")
    for (color in colors) {
        println(color)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/set-of.html)

    