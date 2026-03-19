

# filterIsInstanceTo

Appends all elements that are instances of specified type parameter R to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> Array<*>.filterIsInstanceTo(destination: C): C(source)
```

```kotlin
fun main() {
    val mixedArray = arrayOf(1, "two", 3.0, "four", 5)
    val strings = mutableListOf<String>()

    mixedArray.filterIsInstanceTo(strings)

    println(strings) // Output: [two, four]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-is-instance-to.html)

    