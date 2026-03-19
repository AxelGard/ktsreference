

# createCleaner

Creates a Cleaner object that runs cleanupAction with given resource some time after its deallocation.

```kotlin
@ExperimentalNativeApifun <T> createCleaner(resource: T, cleanupAction: (resource: T) -> Unit): Cleaner(source)
```

import kotlin.native.ref.createCleaner
import kotlin.native.concurrent.gc
import kotlin.native.concurrent.ExperimentalNativeApi

@ExperimentalNativeApi
fun main() {
    class Resource(val name: String) {
        fun close() = println("$name closed")
    }

    var resource: Resource? = Resource("MyResource")
    val cleaner = createCleaner(resource!!) { r -> r.close() }

    println("Using ${resource!!.name}")

    // Drop the only strong reference to the resource
    resource = null

    // Force a GC cycle to trigger the cleaner
    gc()
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.ref/create-cleaner.html)

    