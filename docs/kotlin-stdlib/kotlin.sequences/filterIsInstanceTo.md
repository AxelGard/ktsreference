

# filterIsInstanceTo

Appends all elements that are instances of specified type parameter R to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> Sequence<*>.filterIsInstanceTo(destination: C): C(source)
```

```kotlin
val mixed = sequenceOf(1, "two", 3.0, "four")
val strings = mutableListOf<String>()
mixed.filterIsInstanceTo(strings)
println(strings) // prints: [two, four]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-is-instance-to.html)

    