

# forEachIndexed

Performs the given action on each element, providing sequential index with the element.

```kotlin
inline fun <T> Array<out T>.forEachIndexed(action: (index: Int, T) -> Unit)(source)
```

```kotlin
val colors = arrayOf("Red", "Green", "Blue")

colors.forEachIndexed { index, color ->
    println("Color at index $index is $color")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/for-each-indexed.html)

    