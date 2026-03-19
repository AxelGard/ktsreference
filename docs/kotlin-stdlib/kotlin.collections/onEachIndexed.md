

# onEachIndexed

Performs the given action on each element, providing sequential index with the element, and returns the array itself afterwards.

```kotlin
inline fun <T> Array<out T>.onEachIndexed(action: (index: Int, T) -> Unit): Array<out T>(source)
```

```kotlin
val fruits = arrayOf("Apple", "Banana", "Cherry")

fruits.onEachIndexed { index, fruit ->
    println("Index $index contains $fruit")
}
// Output:
// Index 0 contains Apple
// Index 1 contains Banana
// Index 2 contains Cherry
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/on-each-indexed.html)

    