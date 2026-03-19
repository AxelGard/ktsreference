

# removeAll

Removes all of this collection's elements that are also contained in the specified collection.

```kotlin
@IgnorableReturnValueinline fun <T> MutableCollection<out T>.removeAll(elements: Collection<T>): Boolean(source)
```

```kotlin
val numbers = mutableListOf(1, 2, 3, 4, 5)
val toRemove = listOf(2, 4)

val changed = numbers.removeAll(toRemove)

println(numbers)  // [1, 3, 5]
println(changed)  // true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove-all.html)

    