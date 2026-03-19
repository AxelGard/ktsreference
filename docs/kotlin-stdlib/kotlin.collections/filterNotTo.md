

# filterNotTo

Appends all elements not matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Array<out T>.filterNotTo(destination: C, predicate: (T) -> Boolean): C(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)

    val oddNumbers = mutableListOf<Int>()
    numbers.filterNotTo(oddNumbers) { it % 2 == 0 }

    println(oddNumbers)   // Output: [1, 3, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-not-to.html)

    